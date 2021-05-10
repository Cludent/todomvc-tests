from selene.support.conditions import have, be
from selene.support.shared import browser


class TodoMvcPage:
    base_url = 'https://todomvc4tasj.herokuapp.com'

    def __init__(self):
        self._todos = browser.all('#todo-list>li')

    def open(self, relative_url='/'):
        browser.open(TodoMvcPage.base_url + relative_url)
        app_loaded_require_js = 'return Object.keys(' \
                                'require.s.contexts._.defined).length === 39'
        browser.should(have.js_returned(True, app_loaded_require_js))
        return self

    def open_at_all(self):
        return self.open('/#/')

    def add(self, *names):
        for todo_name in names:
            browser.element('#new-todo').type(todo_name).press_enter()
        return self

    def edit_by_enter(self, name, new_name):
        self._start_editing(name, new_name).press_enter()
        return self

    def edit_by_click_outside(self, name, new_name):
        self._start_editing(name, new_name)
        browser.element('body').click()
        return self

    def edit_by_tab(self, name, new_name):
        self._start_editing(name, new_name).press_tab()
        return self

    def _start_editing(self, name, new_name):
        self._todos.element_by(have.exact_text(name)).double_click()
        return self._todos.element_by(have.css_class('editing'))\
            .element('.edit').with_(set_value_by_js=True).set_value(new_name)

    def cancel_edit(self, name, new_name):
        self._start_editing(name, new_name).press_escape()
        return self

    def toggle(self, name):
        self._todos.element_by(have.exact_text(name))\
            .element('.toggle').click()
        return self

    def clear_completed(self):
        browser.element('#clear-completed').click()
        return self

    def delete(self, name):
        self._todos.element_by(have.exact_text(name)).hover()\
            .element('.destroy').click()
        return self

    def should_have_list(self, *names):
        self._todos.should(have.exact_texts(*names))
        return self

    def should_have_empty_list(self):
        return self.should_have_list()

    def should_have_items_left(self, count):
        browser.element('#todo-count>strong')\
            .should(have.exact_text(str(count)))
        return self

    def should_have_active(self, *names):
        self._todos.filtered_by(have.css_class('active'))\
            .should(have.texts(*names))
        return self

    def should_have_completed(self, *names):
        self._todos.filtered_by(have.css_class('completed'))\
            .should(have.texts(*names))
        return self

    def toggle_all(self):
        browser.element('#toggle-all').click()
        return self

    def should_have_hidden_footer(self):
        browser.element('#footer').should(be.hidden)
        return self
