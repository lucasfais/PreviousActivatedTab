import sublime, sublime_plugin

class PreviousActivatedTabCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    previousView = self.previousView()
    if previousView:
      if self.view_exists(previousView):
        sublime.active_window().focus_view(previousView)
      else:
        self.run(edit)

  def view_exists(self, desired_view):
    for view in sublime.active_window().views():
      if view.id() == desired_view.id():
        return True

  def previousView(self):
    previousView = None
    while not previousView and PreviousViews.previousViews:
      previousView = PreviousViews.previousViews.pop()
    return previousView

class PreviousViews(sublime_plugin.EventListener):
  previousViews = []

  def on_deactivated(self, view):
    self.previousViews.append(view)

  def on_activated(self, view):
    self.remove(view)

  def on_close(self, view):
    self.remove(view)

  def remove(self, view):
    for previousView in self.previousViews:
      if previousView.id() == view.id():
        self.previousViews.remove(previousView)
