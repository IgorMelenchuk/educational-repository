class Trashhold:
    def __init__(self, has_threshold):
        if has_threshold:
            self.threshold = 100000
        else:
            self.threshold = 0

def calculate_bonus(gross_amount, client_rate, recruiter_rate, threshold):
    if client_rate < 1:
        client_amount = gross_amount * 12 * client_rate
    else:
        client_amount = client_rate

    net_amount = client_amount * 0.93
    bonus_without_signing = max(0, (net_amount - threshold) * recruiter_rate)

    bonus_with_signing = bonus_without_signing * 0.55

    return bonus_without_signing, bonus_with_signing

# Example usage
has_threshold_input = input('Есть ли трэшхолд? (yes/no): ').lower()
has_threshold = has_threshold_input == 'yes'

threshold_instance = Trashhold(has_threshold)

gross = int(input('Введите сумму гросс: '))
client_rate = float(input('Введите процент с клиента: '))
recruiter_rate = float(input('Введите ваш процент: '))

bonus_without_signing, bonus_with_signing = calculate_bonus(gross, client_rate, recruiter_rate, threshold_instance.threshold)

print("Recruiter's bonus without signing bonus:", int(bonus_without_signing))
print("Recruiter's bonus with signing bonus:", int(bonus_with_signing))
