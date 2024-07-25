# Сайт с курсом топ-100 криповалют
![image](https://github.com/user-attachments/assets/82da473c-9830-4fbf-b22f-fb72d3971b17)
 
# Стэк 
 + React + scss
 + Flask + flask_caching, flask_cors

# docker-compose
 + backend: (python - guniron)
 + frontend: nginx отдаёт статику (собранный react)
 + nginx: web на порту 81

# Запуск
##### в docker-compose.yml для сервиса backend указать API_KEY
    docker compose up -d


