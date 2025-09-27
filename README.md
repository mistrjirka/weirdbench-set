# weirdbench-set

This is repository encompasing two repos, the first is weird-bench which is a benchmarking utility that can upload to weird-bench-site, the second is weird-bench-site which is a web application to view and compare results from weird-bench. To pull everything you need to pull all the submodules:

```bash
git submodule update --init --recursive
git submodule foreach git checkout main
git submodule foreach git pull origin main
```
