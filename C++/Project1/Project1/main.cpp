#include <iostream>


int main() {
	setlocale(LC_ALL, "RU");

	// ���� ����������
	short a, b;
	std::cout << "������� ���������� A:";
	std::cin >> a; 

	std::cout << "������� ���������� B:";
	std::cin >> b;

	std::cout << "A:" << a << "\nB:" <<b;


	// ���� ������(����� �����)
	short num1 = 1; // -32k - 32k
	unsigned short uns_num = 1; // 2byte / 0 - 65k
	int num2 = 4; // 4byte /-2b - 2b
	long num3 = 5; // 8byte

	// ����� � ������
	float fl_num = 2.223123122f;
	double do_num = 2.21221121212112f; // big range

	// �������� �������
	char sym = '$';


	// ���������� ���

	bool isHappy = true;


	return(0);
}