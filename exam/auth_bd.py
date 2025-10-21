import psycopg2


def connect_to_bd(login, password):
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            dbname="3is",
            user="postgres",
            password="1111"
        )
        cursor = conn.cursor()
        cursor.execute(f"SELECT role, status, password FROM users WHERE login = '{login}'")
        answer = cursor.fetchall()
        print(answer)
        if answer[0][2] == password:
            if answer[0][1] == False:
                return "Ваша учетная запись заблокирована"
            a = answer[0][0]
            return a
        elif len(answer) == 0:
            return "Пользователь не найден"
        else:
            return "Неправильный логин или пароль"
    except:
        return "Error"

def block_user(login):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="3is",
        user="postgres",
        password="1111"
    )
    cursor = conn.cursor()
    cursor.execute(f"UPDATE users set status = {False} WHERE login = '{login}'")
    conn.commit()


if __name__ == "__main__":
    print(connect_to_bd("ChalovD", "Qwerty123!"))
    print(connect_to_bd("KunukAO", "Zxcvbn123!"))
    print(connect_to_bd("KunuAO", "Zxcvbn1!"))