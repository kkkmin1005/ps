#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>

using namespace std;

void get_command(string& command) {

	cout << "1. 행렬 생성" << endl;
	cout << "2. 행렬 출력" << endl;
	cout << "3. 행렬 정렬" << endl;
	cout << "4. 행렬 저장" << endl;
	cout << "0. 프로그램 종료" << endl;

	cin >> command;
}

void get_size(int& size) {
	cin >> size;
}

int** gen_matrix(int size) {
	int** result = new int* [size];
	for (int i = 0; i < size; i++) {
		result[i] = new int[size];
	}

	for (int row = 0; row < size; row++) {
		for (int elem = 0; elem < size; elem++) {
			result[row][elem] = rand() % 100;
		}
	}
	return result;
}

void swap(int* a, int* b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}


void sort_array(int* ary, int size) {
	bool complete = false;

	while (!complete) {
		bool check = true;
		for (int i = 0; i < size - 1; i++) {
			if (ary[i] > ary[i + 1]) {
				swap(ary[i], ary[i + 1]);
				check = false;
			}
		}
		if (check) {
			complete = true;
		}
	}
}

void sort_matrix_row(int** matrix, int size) {
	for (int i = 0; i < size; i++) {
		sort_array(matrix[i], size);
	}
}

void print_matrix(int** matrix, int size) {

	for (int row = 0; row < size; row++) {
		for (int elem = 0; elem < size; elem++) {
			cout << setw(4) << matrix[row][elem];
		}
		cout << endl;
	}
}

void save_matrix(int** matrix, int size, ofstream& temp) {
	temp.open("matrix.txt");

	for (int row = 0; row < size; row++) {
		for (int elem = 0; elem < size; elem++) {
			temp << matrix[row][elem] << " ";
		}
		temp << endl;
	}

	temp.close();
} 

void free_matrix(int** matrix, int size) {
	for (int i = 0; i < size; i++) {
		delete[] matrix[i];
	}
	delete[] matrix;
}

int main() {
	ofstream temp;

	string command;
	int** matrix = NULL;
	int size = 0;
	while (1) {
		get_command(command);
		if (command == "1") {
			get_size(size);
			matrix = gen_matrix(size);
		}
		else if (command == "2") {
			print_matrix(matrix, size);
		}
		else if (command == "3") {
			sort_matrix_row(matrix, size);
		}
		else if (command == "4") {
			save_matrix(matrix, size, temp);
		}
		else if (command == "0") {
			free_matrix(matrix, size);
			cout << "Exit the program.." << endl;
			exit(104);
		}
		else {
			cout << "Wrong command" << endl << endl;
		}
	}
	return 0;
}

//5
//int** create_integer_matrix(int n) {
//	int** result;
//
//	result = new int* [n];
//
//	for (int i = 0; i < n; i++) {
//		result[i] = new int[n];
//	}
//
//	for (int row = 0; row < n; row++) {
//		for (int col = 0; col < n; col++) {
//			result[row][col] = row + col;
//		}
//	}
//	return result;
//}
//
//void destroy_integer_matrix(int** m, int n) {
//	for (int i = 0; i < n; i++) {
//		delete[] m[i];
//	}
//	delete[] m;
//}
//
//int main() {
//
//	int i, j, ** M;
//	M = create_integer_matrix(3);
//
//	for (i = 0; i < 3; i++) {
//		for (j = 0; j < 3;j++) {
//			cout << M[i][j] << " ";
//		}
//		cout << endl;
//	}
//	cout << endl;
//	destroy_integer_matrix(M, 3);
//	return 0;
//}


//4
//int f(int a, int b) {
//	return a + b;
//}
//
//int g(int (*f)(int, int), int x, int y) {
//	return 2 * (*f)(x, y);
//}
//
//int main() {
//	cout << g(f, 2, 3) << endl;
//}


//3
//int main() {
//
//	int a1[10];
//
//	for (int& elem : a1) {
//		elem = 0;
//	}
//
//	*(a1 + 4) = 5;
//
//	for (int i = 0; i < 10; i++) {
//		cout << a1[i];
//	}
//
//	cout << endl;
//
//	int a2[5][10];
//
//	for (int i = 0; i < 5; i++) {
//		for (int j = 0; j < 10; j++) {
//			a2[i][j] = 0;
//		}
//	}
//
//	*(*(a2 + 3) + 4) = 5;
//
//	for (int i = 0; i < 5; i++) {
//		for (int j = 0; j < 10; j++) {
//			cout << a2[i][j];
//		}
//		cout << endl;
//	}
//}