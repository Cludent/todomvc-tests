from selene import command
from selene.support.conditions import have
from selene.support.shared import browser

todos = browser.all('#todo-list>li')


def open():
    browser.open('https://todomvc4tasj.herokuapp.com')
    browser.should(have.js_returned(True, 'return \
            Object.keys(require.s.contexts._.defined).length === 39'))


def add(*names):
    for todo_name in names:
        browser.element('#new-todo').type(todo_name).press_enter()


def edit(name, new_name):
    start_editing(name, new_name).press_enter()


def start_editing(name, new_name):
    todos.element_by(have.exact_text(name)).double_click()
    return todos.element_by(have.css_class('editing')).element('.edit'). \
        perform(command.js.set_value(new_name))


def toggle(name):
    todos.element_by(have.exact_text(name)).element('.toggle').click()


def clear_completed():
    browser.element('#clear-completed').click()


def cancel_edit(name, new_name):
    start_editing(name, new_name).press_escape()


def delete(name):
    todos.element_by(have.exact_text(name)).hover().element('.destroy').click()


def list_should_be(*names):
    todos.should(have.exact_texts(*names))


def set_filter():
    # browser.all('#filters>li').element_by(have.exact_text('All')).should(have.)
    browser.element('#filters>li .selected').click()
    # browser.all('#filters').element_by(have.exact_text('All')).click()
    # browser.all('#filters').element_by(have.css_class('selected')).click()


def items_left_should_be(count):
    browser.element('#todo-count>strong').should(have.exact_text(str(count)))


def active_nums_should_be(count):
    browser.all('#todo-list>li').filtered_by(have.css_class('active')).should(have.size(count))


def completed_nums_should_be(count):
    browser.all('#todo-list>li').filtered_by(have.css_class('completed')).should(have.size(count))


def toggle_all():
    browser.element('#toggle-all').click()
