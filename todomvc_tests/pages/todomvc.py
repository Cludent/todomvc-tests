from selene import command
from selene.support.conditions import have
from selene.support.shared import browser

todos = '#todo-list>li'


def open():
    browser.open('https://todomvc4tasj.herokuapp.com')
    browser.should(have.js_returned(True, 'return \
            Object.keys(require.s.contexts._.defined).length === 39'))


def add(*names):
    for todo_name in names:
        browser.element('#new-todo').type(todo_name).press_enter()


def _find(name):
    return browser.all(todos).element_by(have.exact_text(name))


def edit(name, new_name):
    _start_editing(name, new_name).press_enter()


def _start_editing(name, new_name):
    _find(name).double_click()
    return browser.element('.editing').element('.edit'). \
        perform(command.js.set_value(new_name))


def toggle(name):
    _find(name).element('.toggle').click()


def clear_completed():
    browser.element('#clear-completed').click()


def cancel_edit(name, new_name):
    _start_editing(name, new_name).press_escape()


def delete(name):
    _find(name).hover().element('.destroy').click()


def list_should_match(*names):
    browser.all(todos).should(have.exact_texts(*names))
