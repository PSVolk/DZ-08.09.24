class Shoe:
    def get(self):
        return 'shoe'


class Recipe:
    def get(self):
        return 'recipe'


class Controller:
    def request(self, req):
        if req.lower() == 'shoe':
            s = Shoe()
            return s.get()
        elif req.lower() == 'recipe':
            r = Recipe()
            return r.get()
        else:
            return 'wrong request'


class View:
    def init(self, service):
        self.service = service

    def run(self):
        print('shoe or recipe?')
        r = input()
        print(self.service.request(r))


    if name == 'main':
        service = Controller()
        view = View(service)
        view.run()
class Shoes:
    def init(self, shoe_type, style, color, price, manufacturer, size):
        self.shoe_type = shoe_type
        self.style = style
        self.color = color
        self.price = int(price)
        self.manufacturer = manufacturer
        self.size = int(size)

    def show_shoe(self):
        print(f'Тип обуви: {self.shoe_type}')
        print(f'Вид обуви: {self.style}')
        print(f'Цвет: {self.color}')
        print(f'Цена: {self.price}')
        print(f'Производитель: {self.manufacturer}')
        print(f'Размер: {self.size}')
class Recipe:
    def init(self, name, author, recipe_type, description, link, ingredients, cuisine):
        self.name = name
        self.author = author
        self.recipe_type = recipe_type
        self.description = description
        self.link = link
        self.ingredients = ingredients
        self.cuisine = cuisine

    def show_recipe(self):
        print(f'Название рецепта: {self.name}')
        print(f'Автор рецепта: {self.author}')
        print(f'Тип рецепта: {self.recipe_type}')
        print(f'Текстовое описание рецепта: {self.description}')
        print(f'Ссылка на видео с рецептом: {self.link}')
        print(f'Список ингредиентов: {self.ingredients}')
        print(f'Название кухни: {self.cuisine}')


class Controller:
    def request(self, req):
        if req.lower() == 'обувь':
            s = Shoes('женская', 'кроссовки', 'черный', 1200, 'Спорт', 37)
            return s.show_shoe()
        elif req.lower() == 'рецепты':
            r = Recipe('Борщ украинский', 'FoodTV', 'Первое',
                       'https://www.russianfood.com/recipes/recipe.php?rid=126240',
                       'https://youtu.be/UeSp67Uif1k', 'Продукты', 'Украинская')
            return r.show_recipe()
        else:
            return 'Неверный запрос!'


class View:
    def init(self, service):
        self.service = service

    def run(self):
        print('Обувь или Рецепты? ')
        r = input()
        print(self.service.request(r))


if name == 'main':
    service = Controller()
    view = View(service)
    view.run()