class log_data():
    cal_data = []
    total_cal = 0

    def store_data(self,cal):
        self.cal_data.append(cal)
        self.total_cal += cal