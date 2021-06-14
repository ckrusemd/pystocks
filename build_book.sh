#!/bin/bash
jupyter-book clean .
jupyter-book build .
git pull
git add _build
git add _toc.yml
git add build_book.sh
git add pystocks/stocks/fbprophet/
git add .github/workflows/publish_manual.yml
git commit -m "new build"
git push