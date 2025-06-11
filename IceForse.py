# Оконный интерфейс (tkinter)
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import table_data_sp
import function_iceforce

# Вызов общего окна
window = Tk()
window.title("Расчёт ледовой нагрузки от полей ровного льда")
window.geometry("900x800")

# Вывод заголовка в окне
zag = Label(
    window,
    text="Ввод исходных данных:",
    font=("Arial Bold", 10),
)
zag.grid(column=0, row=0)

# Флаги
b_flag = 0
hd_flag = 0

# Блок подписей вводимых переменных (column 0)

speedtxt = Label(
    window,
    text="Скорость движения ледяного поля ",
    font=("Arial Bold", 10),
)  # Текст скорости движения льда
speedtxt.grid(column=0, row=1, sticky="w")

hdtxt = Label(
    window,
    text="Толщина ровного льда ",
    font=("Arial Bold", 10),
)  # Текст ввода толщины льда
hdtxt.grid(column=0, row=2, sticky="w")

formtxt = Label(
    window,
    text="Форма сооружения в плане: ",
    font=("Arial Bold", 10),
)  # Текст ввода формы сооружжения в плане
formtxt.grid(column=0, row=3, sticky="w")

angletxt = Label(
    window,
    text="Угол заострения сооружения в плане",
    font=("Arial Bold", 10),
)  # Угол заострения опоры в плане_подпись
angletxt.grid(column=0, row=4, sticky="w")

koef_m_txt = Label(
    window, text="Коэффициент формы опоры в плане", font=("Arial Bold", 10)
)
koef_m_txt.grid(column=0, row=5, sticky="w")

b_constr_txt = Label(
    window,
    text="Ширина сооружения на уровне льда",
    font=("Arial Bold", 10),
)  # Угол заострения опоры в плане_подпись
b_constr_txt.grid(column=0, row=6, sticky="w")

ice_field_area_rb = Label(
    window,
    text="Способ ввода площади ледового поля:",
    font=("Arial Bold", 10),
)  # Угол заострения опоры в плане_подпись
ice_field_area_rb.grid(column=0, row=7, sticky="w")

ice_field_area = Label(
    window,
    text="Площадь ледового поля",
    font=("Arial Bold", 10),
)  # Площадь ледового поля
ice_field_area.grid(column=0, row=8, sticky="w")

ice_strength_txt = Label(
    window,
    text="Предел прочности льда при сжатии",
    font=("Arial Bold", 10),
)  # Площадь ледового поля
ice_strength_txt.grid(column=0, row=9, sticky="w")


# Ввод переменных (column 1)
speedobz = Label(
    window,
    text="V = ",
    font=("Arial Bold", 10),
)  # Текст ввода обозначения скорости
speedobz.grid(column=1, row=1, sticky="e")

hdobz = Label(
    window,
    text="hd = ",
    font=("Arial Bold", 10),
)  # Текст ввода обозначения толщины льда
hdobz.grid(column=1, row=2, sticky="e")

angleobz = Label(
    window,
    text="2γ = ",
    font=("Arial Bold", 10),
)  # Угол сооружения в плане
angleobz.grid(column=1, row=4, sticky="e")

b_constr_obz = Label(
    window,
    text="b = ",
    font=("Arial Bold", 10),
)  # Ширина сооружения
b_constr_obz.grid(column=1, row=6, sticky="e")

area_field_obz = Label(
    window,
    text="A = ",
    font=("Arial Bold", 10),
)  # Площадь ледового поля
area_field_obz.grid(column=1, row=8, sticky="e")

ice_strength_obz = Label(
    window,
    text="Rc = ",
    font=("Arial Bold", 10),
)  # Предел прочности льда на сжатие
ice_strength_obz.grid(column=1, row=9, sticky="e")


# Блок вывода единиц измерения (column 3)
ms = "м/с"  # Единицы измерения м/с
m = "м"
edmm1 = Label(window, text=ms, font=("Arial Bold", 10))
edmm1.grid(column=3, row=1)
edmm2 = Label(window, text=m, font=("Arial Bold", 10))
edmm2.grid(column=3, row=2)
edmm_angle = Label(window, text="°", font=("Arial Bold", 10))
edmm_angle.grid(column=3, row=4)
edmm_b = Label(window, text="м", font=("Arial Bold", 10))
edmm_b.grid(column=3, row=6)
edmm_field = Label(window, text="м^2", font=("Arial Bold", 10))
edmm_field.grid(column=3, row=8)
edmm_ice_strength = Label(window, text="МПа", font=("Arial Bold", 10))
edmm_ice_strength.grid(column=3, row=9)




# Блок расчитываемых переменных автоматически (column 1-3)

# Коэффициент формы сооружения в плане m
koef_m_result = Label(
    window, text="m = ", font=("Arial Bold", 10)
)
koef_m_result.grid(column=1, row=5, columnspan=3)




# Блок полей ввода (column 2)

v_speed = Entry(window, width=10)  # окно ввода текста - скорость льда
v_speed.grid(column=2, row=1)  # положение окна ввода текста - скорость льда

hd = Entry(window, width=10)  # окно ввода текста - скорость льда
hd.grid(column=2, row=2)  # положение окна ввода текста - скорость льда
hd.bind("<FocusOut>",lambda e: function_iceforce.hd_func_flag(
        hd, hd_flag
    ),
)

# Выбор формы сооружения в плане для расчёта m
forms = [
    "Треугольник",
    "Многогранник/полуциркульное",
    "Прямоугольник",
]
cbox_form = ttk.Combobox(values=forms)
cbox_form.grid(column=1, row=3, columnspan=3)
cbox_form.bind(
    "<<ComboboxSelected>>",
    lambda event: function_iceforce.koef_m(
        event, forms, cbox_form, koef_m_result, angle
    ),
)

# Ввод угла заострения треугольного сооружения
angle = Entry(
    window, width=10, state="readonly"
)  # окно ввода текста - угол заострения соружения
angle.grid(column=2, row=4)
angle.bind(
    "<FocusOut>",
    lambda e: function_iceforce.m_triang_interpolation(
        table_data_sp.m_triang, angle.get(), koef_m_result
    ),
)

# Ввод ширины сооружения
b_constr = Entry(window, width=10)  # окно ввода текста - ширина сооружения
b_constr.grid(column=2, row=6)

# Ввод площади ледового поля
a_ice_field = Entry(window, width=10)  # окно ввода текста - площадь ледового поля
a_ice_field.grid(column=2, row=8)

# Ввод предела прочности льда на сжатие
ice_strength = Entry(window, width=10)  # Предел прочности льда на сжатие
ice_strength.grid(column=2, row=9)

window.mainloop()  # бесконечный цикл, чтобы окно не закрывалось
