class BonusCalculator:
    def __init__(self, summ_gross, client_percent, grade):
        self.summ_gross = summ_gross
        self.client_percent = client_percent
        self.grade = grade
        self.trashhold = 100000

    def calculate_bonus(self):
        summ_year = self.summ_gross * 12
        summ_net = int(self.summ_gross * 0.87)
        new_summ = int(summ_year * self.client_percent)
        itog = int(new_summ * 0.93)
        bonus = (itog - self.trashhold) * self.grade
        max_signin = int(itog * 0.2)
        bonus2 = int(itog - self.trashhold - max_signin) * self.grade

        return f'Бонус с трешем без сайнина: {int(bonus)}\nБонус с трешем и сайнином: {int(bonus2)}'





