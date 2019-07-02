import cx_Freeze

executables = [cx_Freeze.Executable("goku.py")]

cx_Freeze.setup(
        name = "SnakeYland",
        options={"buid.exe":{"packages":["pygame"],"include_files":["apple.png","snakehead.png","bg2.png","lawn.png"]}},
                
        description = "SnakeYland Game",
        executables = executables


        )
