# Timer

Simple timer CLI app.

Whatever timer app pops up in duckduckgo when you search "timer" is annoying because it doesn't play the sound if you aren't focused on that web page.

I decided I wanted something that would work even if I wasn't focused on it, and I decided it would be best to just have a CLI program I could easily call.

However, I wasn't able to find a simple CLI timer though googling. I'm sure tons exist, but it was surprisingly hard to find. Most "timers" are either pomodoro timers with more features, or are timers like performance related timers like "how long did that program take to execute" instead of timers for alerting you when a certain amount of time has elapsed.

Overall I thought it would be pretty easy to just create something myself.

I looked at some tutorials for inspiration as well.

## Running

You will need to activate the virtual environment in order to have access to the sound player library.

Run the following in the project root dir:

```bash
source venv/bin/activate
```

If setting up for the first time you may need to `pip install` the `requirements.txt`.

You can then run the script (where "m" is minutes and "s" is seconds).

```bash
python3 main.py m:s
```

You can also run the program with `-h` for help (provided by argparse).
