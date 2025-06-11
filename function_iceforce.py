import table_data_sp
import numpy as np
from tkinter import END

# Функции флагов
# Флаг для hd
def hd_b_func_flag(hd_entry, b_constr_entry, kb_table, koef_kb_result):
    hd = hd_entry.get()
    b_constr = b_constr_entry.get()
    if hd and b_constr:  # Проверяем, что поля не пустые
        try:
            hd_val = float(hd)
            b_val = float(b_constr)
            if hd_val != 0 and b_val != 0:
                kb_interpolation(hd_val, b_val, kb_table, koef_kb_result)
        except ValueError:
            pass  # Игнорируем нечисловые значения



# Функция интерполяции значений m, если выбрана форма треугольник
def m_triang_interpolation(table_m_triang, angle_entry, koef_m_result):
    angle_str = angle_entry.get()
    try:
        angle_val = float(angle_str.strip('°'))
        angle_values = np.array(table_m_triang[0]) # Значения угла табличные
        m_values = np.array(table_m_triang[1])   # Значения m табличные
        m = np.interp(angle_val, angle_values, m_values) # Интерполяция значения
        koef_m_str = f"m = {m:.3f}"
        koef_m_result.config(text=koef_m_str) # Вспомогательная подпись для обозначения
    except ValueError:
        pass

# Функция присваивания m при выборе прямоугольной формы и многогранника
def koef_m(event, forms, cbox_form, koef_m_result, angle):
    form_var = cbox_form.get()
    if form_var == forms[2]:  # Прямоугольник
        m = table_data_sp.m_sqad
        angle.config(state="normal") # Разблокируем значение угла
        angle.delete(0, END)  # Очищаем значение угла
        angle.insert(0, "90")
        angle.config(state="disabled")  # Блокируем поле ввода угла
    elif form_var == forms[1]:  # Многогранник
        m = table_data_sp.m_mnog
        angle.config(state="normal") # Разблокируем значение угла
        angle.delete(0, END)  # Очищаем значение угла
        angle.insert(0, "140")
        angle.config(state="readonly")  # Блокируем поле ввода угла
    elif form_var == forms[0]:  # Треугольник
        angle.config(state="normal")
        return  # Не обновляем m, пока не введён угол

    koef_m_str = f"m = {m}"
    koef_m_result.config(text=koef_m_str)

# Функция интерполяции коэффициента kb
def kb_interpolation(hd, b_constr, kb_table, koef_kb_result):
    b_hd_values = np.array(kb_table[0])  # Значения b/hd табличные
    kb_values = np.array(kb_table[1])  # Значения kb табличные
    b_hd = b_constr / hd
    kb = np.interp(b_hd, b_hd_values, kb_values)  # Интерполяция значения
    koef_kb_str = f" (По таблице 18) Коэффициент kb = {kb:.3f}"
    koef_kb_result.config(text=koef_kb_str)  # Вспомогательная подпись для обозначения
