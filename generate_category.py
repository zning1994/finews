import os
import glob
import yaml
import shutil


POSTS_PATH = '_posts'

CATEGORIES_PATH = 'category'
CATEGORY_LAYOUT = 'category'


def get_front_matter(path):
    end = False
    front_matter = ""
    with open(path, 'r') as f:
        for line in f.readlines():
            if line.strip() == '---':
                if end:
                    break
                else:
                    end = True
                    continue
            front_matter += line

    return front_matter


def get_categories():
    all_categories = []

    for file in glob.glob(os.path.join(POSTS_PATH, '*.md')):
        meta = yaml.load(get_front_matter(file))
        try:
            category = meta['categories']
        except KeyError:
            try:
                categories = meta['categories']
            except KeyError:
                err_msg = (
                    "[Error] File:{} at least "
                    "have one category.").format(file)
                print(err_msg)
            else:
                if type(categories) == str:
                    error_msg = (
                        "[Error] File {} 'categories' type"
                        " can not be STR!").format(file)
                    raise Exception(error_msg)

                for ctg in meta['categories']:
                    if ctg not in all_categories:
                        all_categories.append(ctg)
        else:
            if type(category) == list:
                err_msg = (
                    "[Error] File {} 'category' type"
                    " can not be LIST!").format(file)
                raise Exception(err_msg)

            if category not in all_categories:
                all_categories.append(category)

    return all_categories


def generate_category_pages():
    categories = get_categories()
    if os.path.exists(CATEGORIES_PATH):
        shutil.rmtree(CATEGORIES_PATH)

    os.makedirs(CATEGORIES_PATH)

    for category in categories:
        new_page = CATEGORIES_PATH + '/' + category + '.html'
        with open(new_page, 'w+') as html:
            html.write("---\n")
            html.write("layout: {}\n".format(CATEGORY_LAYOUT))
            html.write("title: {}\n".format(category.title()))
            html.write("category: {}\n".format(category))
            html.write("---")
            print("[INFO] Created page: " + new_page)
    print("[INFO] Succeed! {} category-pages created.\n"
          .format(len(categories)))

if __name__ == '__main__':
    generate_category_pages()
