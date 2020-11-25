# Exercise: render-template

We want to create a CLI script that lets us generate files based on a template.
The template can have variables to interpolate in its content and in its
filename.

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
$ ./render-template.py \{firstname\}.template.md
firstname: Louis
linkedin: https://...

./louis.template.md
# Creates a file named louis.template.md, rendering its content with the input variables
```

Note that it does not ask for "today", because this is set to today's date automatically.

## Technical specs

- Only use the standard library. Doc here: https://docs.python.org/3/library/
- The script shouldn't be more than 200 lines long (it is absolutely doable to stay below 70)

## Hints

See [hints.md](./hints.md) (**only if you're stuck!**).
