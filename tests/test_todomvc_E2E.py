from selene.support.shared import browser

from todomvc_tests.pages import todomvc


def test_todos_management():
    browser.config.timeout = 7
    todomvc.open()

    todomvc.add('a', 'b', 'c')
    todomvc.list_should_be('a', 'b', 'c')

    todomvc.edit('a', 'a edited')

    todomvc.toggle('a edited')

    todomvc.clear_completed()
    todomvc.list_should_be('b', 'c')

    todomvc.cancel_edit('b', 'b edited')

    todomvc.delete('b')
    todomvc.list_should_be('c')
