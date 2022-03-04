from plyer import notification

title = "Hello Kedar."

message = "Have a good day."

notification.notify(title=title,
                    message=message,
                    app_icon=None,
                    timeout=10,
                    toast=False)
