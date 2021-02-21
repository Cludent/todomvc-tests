from todomvc_tests.pages import todomvc


def test_todos_management():
    todomvc.visit()
    todomvc.is_all_modules_load()

    todomvc.add('a', 'b', 'c')
    todomvc.is_list_match('a', 'b', 'c')

    todomvc.edit('a', ' edited')
    todomvc.complete('a edited')
    todomvc.clear_completed()
    todomvc.is_list_match('b', 'c')

    todomvc.cancel_edit('b', ' edited')
    todomvc.delete('b')
    todomvc.is_list_match('c')

