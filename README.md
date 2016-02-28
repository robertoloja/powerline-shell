This is a fork of [milkbikis/powerline-shell](https://github.com/milkbikis/powerline-shell), to which I've made modifications.

1. The generated powerline-shell.py no longer uses sys.stdout.write (since print(string, end='') now works.)
  - It also begins with \r, to overwrite any virtualenv info displayed by other scripts.
2. I've added Powerline's branch symbol to the git segment.
3. I fixed the jobs segment, as it was not working for me in fish. 
4. I wrote my own theme.

![Screenshot](http://robertoloja.github.io/screenshot.png)
