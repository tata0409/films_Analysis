# Аналіз даних кіноіндустрії

Цей проєкт виконує аналіз датасету з інформацією про фільми.  
Мета: визначити ключові тренди, популярні жанри, зв'язок між бюджетом та прибутком, а також дослідити зміни популярності фільмів за роками.

## Дані

Використаний датасет містить 45,466 записів і 24 колонки.  
Основні колонки:
- `title`: Назва фільму.
- `release_date`: Дата випуску.
- `budget`: Бюджет фільму.
- `revenue`: Прибуток фільму.
- `genres`: Жанри фільму у форматі JSON.
- `popularity`: Показник популярності.
- `vote_average`: Середня оцінка.

### Очищення даних
1. Видалено записи без дат, з некоректними бюджетами або прибутками.
2. Розділено жанри з JSON-формату на окремі рядки.
3. Додано нові колонки: `release_year` (рік випуску).

## Результати

### 1. Популярність жанрів
Графік нижче демонструє кількість фільмів для кожного жанру. Найпопулярніші жанри:
- **Drama**
- **Comedy**
- **Thriller**

![Популярність жанрів](genre_popularity.png)

### 2. Тренди популярності
З роками популярність фільмів росте. Це видно з графіка середньої популярності фільмів за роками:

![Тренди популярності](popularity_trend.png)

### 3. Бюджет та прибуток
Залежність між бюджетом і прибутком показує, що високобюджетні фільми зазвичай більш прибутні:

![Бюджет vs Прибуток](budget_vs_profit.png)

## Як повторити аналіз?

1. **Завантажте репозиторій**:
   ```bash
   git clone [<URL-репозиторію>](https://github.com/tata0409/films_Analysis/)

2. Встановіть залежності: Переконайтеся, що у вас встановлено Python 3.8+ та бібліотеки:

bash
Копировать код
pip install pandas matplotlib seaborn



---

```markdown
## Контакти

Якщо у вас є запитання, пишіть на email: tatachechyna@gmail.com.

Дякуємо, що зацікавилися нашим проєктом!
