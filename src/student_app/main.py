try:
    from .config import APP_NAME, DEBUG, MAX_STUDENTS
except ImportError:
    from config import APP_NAME, DEBUG, MAX_STUDENTS


def main():
    print("Application Starting...")
    print()

    print(f"Application Name: {APP_NAME}")
    print(f"Debug Mode: {DEBUG}")
    print(f"Maximum Students: {MAX_STUDENTS}")


if __name__ == "__main__":
    main()