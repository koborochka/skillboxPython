import copy


def replace_product_name(template, product_name):
    if isinstance(template, str):
        return template.replace('телефон', product_name).replace('iPhone', product_name)
    elif isinstance(template, dict):
        new_template = {}
        for key, value in template.items():
            new_template[key] = replace_product_name(value, product_name)
        return new_template
    else:
        return template


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

num_sites = int(input("Сколько сайтов: "))
sites_template = [copy.deepcopy(site) for _ in range(num_sites)]
product_names_list = []

for i in range(num_sites):
    product_name = input("Введите название продукта для нового сайта: ")
    product_names_list.append(product_name)
    for j in range(i + 1):
        cur_product_name = product_names_list[j]
        print(f"Сайт для {cur_product_name}: ")
        print(replace_product_name(sites_template[j], cur_product_name))