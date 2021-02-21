from selene.support.conditions import have
from selene.support.shared import browser
browser.config.timeout = 7

todo_list = '#todo-list>li'


def visit():
    browser.open('https://todomvc4tasj.herokuapp.com')


def is_all_modules_load():
    browser.should(have.js_returned(True, 'return \
        Object.keys(require.s.contexts._.defined).length === 39'))


def add(*todo_names):
    for todo_name in todo_names:
        browser.element('#new-todo').type(todo_name).press_enter()


def edit(todo_name, new_name):
    browser.all(todo_list).element_by(have.exact_text(todo_name)) \
        .double_click()
    browser.all(todo_list).element_by(have.css_class('editing')) \
        .element('.edit').type(new_name).press_enter()


def complete(todo_name):
    browser.all(todo_list).element_by(have.exact_text(todo_name)) \
        .element('.toggle').click()


def clear_completed():
    browser.element('#clear-completed').click()


def cancel_edit(todo_name, new_name):
    browser.all(todo_list).element_by(have.exact_text(todo_name)) \
            .double_click()
    browser.all(todo_list).element_by(have.css_class('editing')) \
        .element('.edit').type(new_name).press_escape()


def delete(todo_name):
    browser.all(todo_list).element_by(have.exact_text(todo_name)) \
        .hover().element('.destroy').click()


def is_list_match(*todo_names):
    browser.all(todo_list).should(have.exact_texts(*todo_names))
