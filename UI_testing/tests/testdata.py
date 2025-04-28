
login_test_data = [
    ("project_practice@gmail.com", "0123456", True),
    ("project_practice@gmail.com", "789456", False),
    ("", "", False),
    ("project_practice@gmail.com", "", False),
    ("", "0123456", False),
    (" project_practice @gmail.com", "0123456", False),
    ("project_practice@gmail.com", "        ", False),
]


register_test_data = [
    # email,     password,    confirm password,     name,       expected inline errors (in order)
    ("",               "",          "",          "",         [
        "Email address is required",
        "Password is required",
        "Confirm Password is required",
        "Name is required",
    ]),
    ("karolina@gmail.com", "",      "",          "",         [
        "Password is required",
        "Confirm Password is required",
        "Name is required",
    ]),
    ("",               "",          "",          "Karolina", [
        "Email address is required",
        "Password is required",
        "Confirm Password is required",
    ]),
    ("karolina.gmail.com", "",      "",          "",         [
        "Email address is invalid",
    ]),
    ("karolina@gmail.com", "4567890","",         "Karolina", [
        "Confirm Password is required",
    ]),
    ("karolina@gmail.com", "4567890", "987654",   "Karolina", [
        "Passwords do not match",
    ]),
    ("karolina@gmail.com", "456",     "456",      "Karolina", [
        "Password must be between 6 and 30 characters",
    ]),
    ("karolina@gmail.com", "4567890", "4567890",  "Ker",     [
        "User name should be between 4 and 30 characters",
    ]),
    ("karolina@gmail.com", "4567890","4567890",  "Karolina", [
        "Email already exists",
    ]),
    ("      ",         "      ",    "      ",    "      ",  [
        "Email address is required",
        "Password is required",
        "Confirm Password is required",
        "Name is required",
    ]),
]