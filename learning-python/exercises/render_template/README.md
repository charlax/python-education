# Exercise: render-template

We want to create a CLI script that lets us generate files based on a template.

The template can have variables to interpolate in its content and in its
filename.

This should take less than 2 hours.

There is a skeleton for the script in
[render-template.py](./render-template.py).

## Exercise objective

This is a very complete exercise:

- Write simple functions
- Create a CLI script in Python
- Use some standard lib modules
- Use loops
- Use standard input and output
- Raise errors
- Use datetime
- Read and write to files
- Interpolate variables in string
- Manipulate dicts and sets
- Optional: functional programming in Python
- It's actually a useful script!

## Example usage

[![asciicast](https://asciinema.org/a/tFkycU36PgYwDTvRqr6FBCa7B.svg)](https://asciinema.org/a/tFkycU36PgYwDTvRqr6FBCa7B)

Say we have this template file, named `{firstname}.template.md`:

```md
# Interview for {firstname}

Date: {today}

LinkedIn : {linkedin}
```

We use it like this:

```bash
$ ./render-template.py \{firstname\}.\{lastname\}template.md
firstname: Louis
lastname: de Funès
linkedin: https://...

./louis.de_funès.md
# Creates a file named louis.de_funès.md, rendering its content with the input variables
```

- Note that it does not ask for "today", because this is set to today's date automatically.
- Variable prompts are sorted by alphabetical order.

## Technical specs

- Only use the standard library. Doc here: https://docs.python.org/3/library/
- The script shouldn't be more than 200 lines long (it is absolutely doable to stay below 70)

## Hints

See [hints.md](./hints.md) (**only if you're stuck!**).
