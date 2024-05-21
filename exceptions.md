## Exception Handling

In our project we create plots that display information about the data.
We use the `matplotlib` library to create these plots. In order to prevent errors from happneing,
we use the `try` and `except` blocks to handle exceptions.

```python
try:
    # code that creates the data for the plots and the plots
except Exception as e:
    # code that creates a error message for the user if an error occured
```

If an errors occurs during the selection of the data, creating of the summary statics, or creation of the plots,
we will catch the error and display a message to the user.
The message will inform the user that an error occured and prompt the user to refresh the site, 
which will go back to the default view, where no errors should occur.