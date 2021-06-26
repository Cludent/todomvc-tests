from todomvc_tests.pages import todomvc


def test_todos_management():
    todomvc.open()

    todomvc.add('a', 'b', 'c')
    todomvc.should_have_list('a', 'b', 'c')

    todomvc.edit_by_enter('a', 'a edited')

    todomvc.toggle('a edited')

    todomvc.clear_completed()
    todomvc.should_have_list('b', 'c')

    todomvc.cancel_edit('b', 'b edited')

    todomvc.delete('b')
    todomvc.should_have_list('c')


def test_todos_management1():
    todomvc.open()

    todomvc.add('a', 'b', 'c')
    todomvc.should_have_list('a', 'b', 'c')

    todomvc.edit_by_enter('a', 'a edited')

    todomvc.toggle('a edited')

    todomvc.clear_completed()
    todomvc.should_have_list('b', 'c')

    todomvc.cancel_edit('b', 'b edited')

    todomvc.delete('b')
    todomvc.should_have_list('c')
