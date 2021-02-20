from selene.support.conditions import have
from selene.support.shared import browser
browser.config.timeout = 7


def test_todos_management():
    browser.open('https://todomvc4tasj.herokuapp.com')
    browser.should(have.js_returned(True, 'return \
        Object.keys(require.s.contexts._.defined).length === 39'))

    # Add
    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

    # Edit
    browser.all('#todo-list>li').element_by(have.exact_text('a')).double_click()
    browser.all('#todo-list>li').element_by(have.css_class('editing'))\
        .element('.edit').type(' edited').press_enter()

    # Complete
    browser.all('#todo-list>li').element_by(have.exact_text('a edited'))\
        .element('.toggle').click()

    # Clear completed
    browser.element('#clear-completed').click()
    browser.all('#todo-list>li').should(have.exact_texts('b', 'c'))

    # Cancel edit
    browser.all('#todo-list>li').element_by(have.exact_text('b')).double_click()
    browser.all('#todo-list>li').element_by(have.css_class('editing'))\
        .element('.edit').type(' edited').press_escape()

    # Delete
    browser.all('#todo-list>li').element_by(have.exact_text('b')).hover()\
        .element('.destroy').click()
    browser.all('#todo-list>li').should(have.exact_texts('c'))
