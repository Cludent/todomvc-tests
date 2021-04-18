from selene.support.conditions import have
from selene.support.shared import browser

from todomvc_tests.pages import todomvc
'''
suppositions:
- testing both editing by change focus variants because there is no information
on how the developers implemented this feature. There is a possibility that
changing focus by clicking outside will not work, or vice versa 
- implicitly check 'Clear complete' button visibility in 'test_clear_completed'
- implicitly check footer visibility in method 'items_left_should_be()'
- don't use controls to follow the principles of KISS
'''


def test_add_first():
    todomvc.open()

    # WHEN nothing
    todomvc.add()

    todomvc.should_have_empty_list()
    todomvc.should_have_hidden_footer()

    # WHEN one
    todomvc.add('a')

    todomvc.should_have_list('a')
    todomvc.should_have_items_left(1)


def test_add_many():
    todomvc.open()

    todomvc.add('a', 'b', 'c')

    todomvc.should_have_list('a', 'b', 'c')
    todomvc.should_have_items_left(3)


def test_edit_by_enter():
    todomvc.open().add('a', 'b', 'c')

    todomvc.edit_by_enter('b', 'b edited')

    todomvc.should_have_list('a', 'b edited', 'c')
    todomvc.should_have_items_left(3)


def test_edit_by_click_outside():
    todomvc.open().add('a', 'b', 'c')

    todomvc.edit_by_click_outside('b', 'b edited')

    todomvc.should_have_list('a', 'b edited', 'c')
    todomvc.should_have_items_left(3)


def test_edit_by_tab():
    todomvc.open().add('a', 'b', 'c')

    todomvc.edit_by_tab('b', 'b edited')

    todomvc.should_have_list('a', 'b edited', 'c')
    todomvc.should_have_items_left(3)


def test_cancel_edit_by_esc():
    todomvc.open().add('a', 'b', 'c')

    todomvc.cancel_edit('b', 'b edited')

    todomvc.should_have_list('a', 'b', 'c')
    todomvc.should_have_items_left(3)


def test_delete_by_edit_to_blank():
    todomvc.open().add('a', 'b', 'c')

    todomvc.edit_by_enter('b', '')

    todomvc.should_have_list('a', 'c')
    todomvc.should_have_items_left(2)


def test_complete():
    todomvc.open().add('a', 'b', 'c')

    todomvc.toggle('b')

    todomvc.should_have_items_left(2)
    todomvc.should_have_active('a', 'c')
    todomvc.should_have_completed('b')


def test_complete_all():
    todomvc.open().add('a', 'b', 'c')

    todomvc.toggle_all()

    todomvc.should_have_items_left(0)
    todomvc.should_have_active()
    todomvc.should_have_completed('a', 'b', 'c')


def test_clear_completed():
    todomvc.open().add('a', 'b', 'c', 'd')\
        .toggle('b')\
        .toggle('c')

    todomvc.clear_completed()

    todomvc.should_have_list('a', 'd')
    todomvc.should_have_items_left(2)


def test_activate():
    todomvc.open().add('a', 'b', 'c')\
        .toggle('b')

    todomvc.toggle('b')

    todomvc.should_have_items_left(3)
    todomvc.should_have_active('a', 'b', 'c')
    todomvc.should_have_completed()


def test_activate_all():
    todomvc.open().add('a', 'b', 'c')\
        .toggle_all()

    todomvc.toggle_all()

    todomvc.should_have_items_left(3)
    todomvc.should_have_active('a', 'b', 'c')
    todomvc.should_have_completed()


def test_delete():
    todomvc.open()

    # delete one
    todomvc.add('a')\
        .delete('a')

    todomvc.should_have_hidden_footer()
    todomvc.should_have_empty_list()

    # delete many
    todomvc.add('a', 'b', 'c', 'd')\
        .delete('b')\
        .delete('c')

    todomvc.should_have_items_left(2)
    todomvc.should_have_list('a', 'd')
