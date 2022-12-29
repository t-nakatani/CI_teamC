# CI_teamC
先端ソフトCチーム課題用リポジトリ

### Dokcer環境での動作手順
.envファイルを`CI_teamC`直下に配置

```sh
docker build -t realtime_kansai .
```
```sh
docker run --rm -it -p 9090:9090 -v $(pwd):/work realtime_kansai python manage.py runserver 0.0.0.0:9090
```
http://localhost:9090/ にアクセス