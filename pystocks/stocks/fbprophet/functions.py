from fredapi import Fred
import pandas as pd
import plotly.express as plt
from fbprophet import Prophet
from fbprophet.plot import add_changepoints_to_plot, plot_plotly
from fbprophet.diagnostics import cross_validation, performance_metrics
import itertools
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.dates import (
    MonthLocator,
    num2date,
    AutoDateLocator,
    AutoDateFormatter,
)
from matplotlib.ticker import FuncFormatter
from datetime import datetime
from pandas_datareader.data import DataReader

def subtract_one_month(timestamp):
    import datetime
    return( timestamp - datetime.timedelta(days=30) )

def subtract_one_year(timestamp):
    import datetime
    return( timestamp - datetime.timedelta(days=365) )
    
def collect_tune_and_predict(item,n_ahead = 365):
    param_grid =    {  
            'changepoint_prior_scale': [0.001, 0.01, 0.1, 0.5, 1],
            'seasonality_prior_scale': [0.01, 0.1, 1.0, 10.0, 20.0]
                        }
    # Get Data
    data = DataReader(item,  "yahoo", datetime(1900,1,1), datetime.now())
    data = pd.DataFrame(data)
    data.index.name = 'ds'
    data.reset_index(inplace=True)
    data = data.dropna()
    data = data.rename(columns={'Close' : 'y'})

    # Tune
    all_params = [dict(zip(param_grid.keys(), v)) for v in itertools.product(*param_grid.values())]
    rmses = [] 
    # Use cross validation to evaluate all parameters
    latest_date = data.tail(1).iloc[0]['ds']
    cutoffs = [ subtract_one_month( latest_date ) ]
    for params in all_params:
        m = Prophet(**params).fit(data)  # Fit model with given params
        df_cv = cross_validation(m, cutoffs=cutoffs, horizon='30 days', parallel="processes")
        df_p = performance_metrics(df_cv, rolling_window=1)
        rmses.append(df_p['rmse'].values[0])

    # Rolling windows
    # Find the best parameters
    tuning_results = pd.DataFrame(all_params)
    tuning_results['rmse'] = rmses
    # Python
    best_params = all_params[np.argmin(rmses)]

    # Python
    m = Prophet(**best_params)
    m.fit(data)

    best_params['rmse'] = min( rmses )
    print(best_params)
    # Python
    future = m.make_future_dataframe(periods=365)
    forecast = m.predict(future)
    # SMA
    sma = pd.DataFrame(data = { 
                                'ds' : data['ds'], 
                                'SMA_50' : data['y'].rolling(window=50,min_periods=1).mean(), 
                                'SMA_100' : data['y'].rolling(window=100,min_periods=1).mean(),
                                'SMA_200' : data['y'].rolling(window=200,min_periods=1).mean()
    })
    # Join SMA
    forecast = pd.merge(forecast,sma,on='ds',how='left')
    fig1 = plot_(m,forecast)
    a = add_changepoints_to_plot(fig1.gca(), m, forecast)
    # Python
    fig2 = m.plot_components(forecast)

    # Latest 365
    future = m.make_future_dataframe(periods=30)
    forecast = m.predict(future)
    forecast = pd.merge(forecast,sma,on='ds',how='left')
    forecast = forecast[forecast['ds'] >= subtract_one_year( datetime.today() )]
    m.history = m.history[m.history['ds'] >= subtract_one_year( datetime.today() )]
    fig3 = plot_(m,forecast)
    return( { 'fig1' : fig1, 'fig2' : fig2, 'fig3': fig3})


def plot_(
    m, fcst, ax=None, uncertainty=True, plot_cap=True, xlabel='ds', ylabel='y',
    figsize=(10, 6), include_legend=False
):
    """Plot the Prophet forecast.
    Parameters
    ----------
    m: Prophet model.
    fcst: pd.DataFrame output of m.predict.
    ax: Optional matplotlib axes on which to plot.
    uncertainty: Optional boolean to plot uncertainty intervals, which will
        only be done if m.uncertainty_samples > 0.
    plot_cap: Optional boolean indicating if the capacity should be shown
        in the figure, if available.
    xlabel: Optional label name on X-axis
    ylabel: Optional label name on Y-axis
    figsize: Optional tuple width, height in inches.
    include_legend: Optional boolean to add legend to the plot.
    Returns
    -------
    A matplotlib figure.
    """
    if ax is None:
        fig = plt.figure(facecolor='w', figsize=figsize)
        ax = fig.add_subplot(111)
    else:
        fig = ax.get_figure()
    fcst_t = fcst['ds'].dt.to_pydatetime()
    ax.plot(m.history['ds'].dt.to_pydatetime(), m.history['y'], 'k.',
            label='Observed data points')
    ax.plot(fcst_t, fcst['yhat'], ls='-', c='#0072B2', label='Forecast')
    if 'cap' in fcst and plot_cap:
        ax.plot(fcst_t, fcst['cap'], ls='--', c='k', label='Maximum capacity')
    if m.logistic_floor and 'floor' in fcst and plot_cap:
        ax.plot(fcst_t, fcst['floor'], ls='--', c='k', label='Minimum capacity')
    if uncertainty and m.uncertainty_samples:
        ax.fill_between(fcst_t, fcst['yhat_lower'], fcst['yhat_upper'],
                        color='#0072B2', alpha=0.2, label='Uncertainty interval')
    # Specify formatting to workaround matplotlib issue #12925
    locator = AutoDateLocator(interval_multiples=False)
    formatter = AutoDateFormatter(locator)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    ax.grid(True, which='major', c='gray', ls='-', lw=1, alpha=0.2)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    # SMA
    ax.plot(fcst['ds'],fcst['SMA_50'] )
    ax.plot(fcst['ds'],fcst['SMA_100'] )
    ax.plot(fcst['ds'],fcst['SMA_200'] )
    if include_legend:
        ax.legend()
    fig.tight_layout()
    return fig


