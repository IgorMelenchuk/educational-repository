#include <iostream>


int main() {
	setlocale(LC_ALL, "RU");

	// Типы переменных
	short a, b;
	std::cout << "Введите переменную A:";
	std::cin >> a; 

	std::cout << "Введите переменную B:";
	std::cin >> b;

	std::cout << "A:" << a << "\nB:" <<b;


	// Типы данных(целые числа)
	short num1 = 1; // -32k - 32k
	unsigned short uns_num = 1; // 2byte / 0 - 65k
	int num2 = 4; // 4byte /-2b - 2b
	long num3 = 5; // 8byte

	// Числа с точкой
	float fl_num = 2.223123122f;
	double do_num = 2.21221121212112f; // big range

	// Хранение символа
	char sym = '$';


	// Логический тип

	bool isHappy = true;


	return(0);
}