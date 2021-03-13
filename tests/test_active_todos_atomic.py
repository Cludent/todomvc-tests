from selene.support.conditions import have
from selene.support.shared import browser
from todomvc_tests.pages import todomvc


def test_add():
    browser.config.timeout = 7
    todomvc.open()
    todomvc.add('a', 'b', 'c')
    todomvc.set_filter()
    todomvc.list_should_be('a', 'b', 'c')
    todomvc.items_left_should_be(3)
    todomvc.active_nums_should_be(3)
    todomvc.completed_nums_should_be(0)
    browser.close()


def test_edit_finish_by_enter():
    browser.config.timeout = 7
    todomvc.open()
    todomvc.add('a', 'b', 'c')
    todomvc.set_filter()
    todomvc.start_editing('a', 'a edited').press_enter()
    todomvc.list_should_be('a edited', 'b', 'c')
    todomvc.items_left_should_be(3)
    todomvc.active_nums_should_be(3)
    todomvc.completed_nums_should_be(0)
    browser.close()


def test_edit_finish_by_click_outside():
    browser.config.timeout = 7
    todomvc.open()
    todomvc.add('a', 'b', 'c')
    todomvc.set_filter()
    todomvc.start_editing('a', 'a edited')
    todomvc.todos.element_by(have.exact_text('b')).click()
    todomvc.list_should_be('a edited', 'b', 'c')
    todomvc.items_left_should_be(3)
    todomvc.active_nums_should_be(3)
    todomvc.completed_nums_should_be(0)
    browser.close()


def test_edit_finish_by_tab():
    browser.config.timeout = 7
    todomvc.open()
    todomvc.add('a', 'b', 'c')
    todomvc.set_filter()
    todomvc.start_editing('a', 'a edited').press_tab()
    todomvc.list_should_be('a edited', 'b', 'c')
    todomvc.items_left_should_be(3)
    todomvc.active_nums_should_be(3)
    todomvc.completed_nums_should_be(0)
    browser.close()


def test_cancel_edit_by_esc():
    browser.config.timeout = 7
    todomvc.open()
    todomvc.add('a', 'b', 'c')
    todomvc.set_filter()
    todomvc.cancel_edit('b', 'b edited')
    todomvc.list_should_be('a', 'b', 'c')
    todomvc.items_left_should_be(3)
    todomvc.active_nums_should_be(3)
    todomvc.completed_nums_should_be(0)
    browser.close()


def test_delete_by_edit_to_blank():
    browser.config.timeout = 7
    todomvc.open()
    todomvc.add('a', 'b', 'c')
    todomvc.set_filter()
    todomvc.start_editing('a', '').press_enter()
    todomvc.list_should_be('b', 'c')
    todomvc.items_left_should_be(2)
    todomvc.active_nums_should_be(2)
    todomvc.completed_nums_should_be(0)
    browser.close()


def test_complete():
    browser.config.timeout = 7
    todomvc.open()
    todomvc.add('a', 'b', 'c')
    todomvc.set_filter()
    todomvc.toggle('b')
    todomvc.list_should_be('a', 'b', 'c')
    todomvc.items_left_should_be(2)
    todomvc.active_nums_should_be(2)
    todomvc.completed_nums_should_be(1)
    browser.close()


def test_complete_all():
    browser.config.timeout = 7
    todomvc.open()
    todomvc.add('a', 'b', 'c')
    todomvc.items_left_should_be(3)
    todomvc.set_filter()
    todomvc.toggle_all()
    todomvc.list_should_be('a', 'b', 'c')
    todomvc.items_left_should_be(0)
    todomvc.active_nums_should_be(0)
    todomvc.completed_nums_should_be(3)
    browser.close()


def test_clear_completed():
    browser.config.timeout = 7
    todomvc.open()
    todomvc.add('a', 'b', 'c')
    todomvc.set_filter()
    todomvc.toggle('a')
    todomvc.toggle('b')
    todomvc.clear_completed()
    todomvc.list_should_be('c')
    todomvc.items_left_should_be(1)
    todomvc.active_nums_should_be(1)
    todomvc.completed_nums_should_be(0)
    browser.close()


def test_activate():
    browser.config.timeout = 7
    todomvc.open()
    todomvc.add('a', 'b', 'c')
    todomvc.set_filter()
    todomvc.toggle('b')
    todomvc.completed_nums_should_be(1)
    todomvc.toggle('b')
    todomvc.list_should_be('a', 'b', 'c')
    todomvc.active_nums_should_be(3)
    todomvc.completed_nums_should_be(0)
    browser.close()


def test_activate_all():
    browser.config.timeout = 7
    todomvc.open()
    todomvc.add('a', 'b', 'c')
    todomvc.items_left_should_be(3)
    todomvc.set_filter()
    todomvc.toggle_all()
    todomvc.completed_nums_should_be(3)
    todomvc.toggle_all()
    todomvc.list_should_be('a', 'b', 'c')
    todomvc.items_left_should_be(3)
    todomvc.active_nums_should_be(3)
    todomvc.completed_nums_should_be(0)
    browser.close()


def test_delete():
    browser.config.timeout = 7
    todomvc.open()
    todomvc.add('a', 'b', 'c')
    todomvc.set_filter()
    todomvc.delete('b')
    todomvc.list_should_be('a', 'c')
    todomvc.items_left_should_be(2)
    todomvc.active_nums_should_be(2)
    todomvc.completed_nums_should_be(0)
    browser.close()


# def test_switch_
