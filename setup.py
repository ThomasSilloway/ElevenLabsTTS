from cx_Freeze import setup, Executable

setup(name="elevenlabstts",
      version="0.0.1",
      description="Output audio from text using elevenlabs tts",
      executables=[Executable("src/main.py")],
      options={"build_exe": {"include_files": ["src", "config"]}},
      )
