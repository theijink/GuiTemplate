import non_glue.commandline
import non_glue.environment
from behave import given, when, then, step

@given("the virtual environment {venv_name} is activated")
def step_impl(context, venv_name):
    context.venv_name=venv_name
    response = non_glue.environment.deactivate_and_activate_venv(context.venv_name)
    py_exec_path = non_glue.environment.get_python_executable()
    assert venv_name in py_exec_path, 'Expected venv {} is not part of executable path {}'.format(venv_name, py_exec_path)


@given("the {library_name} library is imported")
def step_impl(context, library_name):
    context.library_name=library_name
    globals()[context.library_name]=__import__(context.library_name)
    assert context.library_name in globals(), 'Expected library {} not found in globals list {}'.format(context.library_name, globals())
    assert context.library_name+'.py' in str(eval(context.library_name)), 'Expected source code {} in module root {}'.format(context.library_name+'.py', str(eval(context.library_name)))


@when("the {class_name} class is called")
def step_impl(context, class_name):
    context.class_name=class_name
    context.object=getattr(eval(context.library_name), context.class_name)

@then("a window should pop up")
def step_impl(context):
    
    assert context.library_name+'.'+context.class_name in str(type(context.object())), 'Expected {} to consist out of {} class.'.format(str(type(context.object())), context.library_name+'.'+context.class_name)

