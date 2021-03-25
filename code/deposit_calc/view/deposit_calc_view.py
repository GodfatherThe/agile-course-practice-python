import tkinter as tk

from deposit_calc.viewmodel import viewmodel


class GUIView(object):

    view_model = viewmodel.DepositCalcViewModel()
    N_LOG_MESSAGES_TO_DISPLAY = 8

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Deposit Calculator')
        self.root.geometry('900x600')
        self.root.resizable(width=False, height=False)

        self.frame = tk.Frame(self.root)
        self.start_message = tk.Label(self.root, text="fill in the fields")
        self.start_depo = tk.Label(self.root, text="Input start deposit:")
        self.start_depo_value = tk.Entry(self.root, width=50)
        self.depo_time = tk.Label(self.root, text="Input deposit time:")
        self.depo_time_value = tk.Entry(self.root, width=50)
        self.interest_rate = tk.Label(self.root, text="Input interest rate:")
        self.rate_value = tk.Entry(self.root, width=50)
        self.capitalization_frequency = tk.Label(self.root, text="Input capitalization frequency:")
        self.capitalization_value = tk.Entry(self.root, width=50)
        self.replenishment_freq = tk.Label(self.root, text="Input replenishment frequency:")
        self.replenishment_freq_value = tk.Entry(self.root, width=50)
        self.replenishment_size = tk.Label(self.root, text="Input replenishment size:")
        self.replenishment_size_value = tk.Entry(self.root, width=50)

        self.handle_btn = tk.Button(self.root, text="handle", state='disabled')
        self.result_label = tk.Label(self.root, text="Result:")
        self.result = tk.Entry(self.root, width=50)

        self.lbl_result = tk.Label(self.root, text="Here will be your result")

        self.set_weight_to_grid()
        self.bind_events()
        self.root.mainloop()

    def set_weight_to_grid(self):
        self.root.grid_rowconfigure(1, minsize=30)
        self.root.grid_rowconfigure(3, minsize=30)
        self.root.grid_rowconfigure(5, minsize=30)
        self.frame.place(relx=0.2, rely=0.2, relwidth=0.8, relheight=0.8)
        self.start_message.grid(row=0, column=0, stick='wens', padx=5, pady=5)

        self.start_depo.grid(row=2, column=0, stick='wens', padx=5, pady=5)
        self.start_depo_value.grid(row=2, column=1, stick='wens', padx=5, pady=5)
        self.depo_time.grid(row=4, column=0, stick='wens', padx=5, pady=5)
        self.depo_time_value.grid(row=4, column=1, stick='wens', padx=5, pady=5)
        self.interest_rate.grid(row=6, column=0, stick='wens', padx=5, pady=5)
        self.rate_value.grid(row=6, column=1, stick='wens', padx=5, pady=5)
        self.capitalization_frequency.grid(row=8, column=0, stick='wens', padx=5, pady=5)
        self.capitalization_value.grid(row=8, column=1, stick='wens', padx=5, pady=5)
        self.replenishment_freq.grid(row=10, column=0, stick='wens', padx=5, pady=5)
        self.replenishment_freq_value.grid(row=10, column=1, stick='wens', padx=5, pady=5)
        self.replenishment_size.grid(row=12, column=0, stick='wens', padx=5, pady=5)
        self.replenishment_size_value.grid(row=12, column=1, stick='wens', padx=5, pady=5)

        self.handle_btn.grid(row=14, column=1, stick='wens', padx=5, pady=5)

        self.result_label.grid(row=16, column=0, stick='wens', padx=5, pady=5)
        self.result.grid(row=16, column=1, stick='wens', padx=5, pady=5)

        self.lbl_result.grid(row=17, column=0, stick='wens', padx=5, pady=5)

    def bind_events(self):
        self.start_depo_value.bind('<KeyRelease>', self.start_depo_changed)
        self.depo_time_value.bind('<KeyRelease>', self.depo_time_changed)
        self.rate_value.bind('<KeyRelease>', self.rate_value_changed)
        self.capitalization_value.bind('<KeyRelease>', self.capitalization_changed)
        self.replenishment_freq_value.bind('<KeyRelease>', self.replenishment_freq_changed)
        self.replenishment_size_value.bind('<KeyRelease>', self.replenishment_size_changed)
        self.handle_btn.bind('<Button-1>', self.handle_btn_clicked)

    def start_depo_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def depo_time_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def rate_value_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def capitalization_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def replenishment_freq_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def replenishment_size_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def handle_btn_clicked(self, event):
        self.mvvm_bind()
        self.view_model.handle_btn_clicked()
        self.mvvm_back_bind()

    def mvvm_bind(self):
        self.view_model.set_start_depo(self.start_depo_value.get())
        self.view_model.set_depo_time(self.depo_time_value.get())
        self.view_model.set_rate(self.rate_value.get())
        self.view_model.set_capitalization(self.capitalization_value.get())
        self.view_model.set_replenishment_freq(self.replenishment_freq_value.get())
        self.view_model.set_replenishment_size(self.replenishment_size_value.get())

    def mvvm_back_bind(self):
        self.handle_btn.config(
            state=self.view_model.get_handle_btn_state())
        self.result.delete(0, tk.END)
        self.result.insert(tk.END, self.view_model.get_result())
        logger_text = '\n'.join(
            self.view_model.logger.get_log_messages()[:-self.N_LOG_MESSAGES_TO_DISPLAY:-1])
        self.lbl_result.config(text=logger_text)
