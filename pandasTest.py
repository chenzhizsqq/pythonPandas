# 手动重新生成Excel文件数据，包含C++和Kotlin代码对比
import pandas as pd  # 确保导入 pandas 库

# 数据：C++ 和 Kotlin 基本用法对比
data_usage_manual = {
    "Feature": [
        "Hello World", "Variable Declaration", "Conditional Statements", 
        "Loops", "Functions", "OOP (Classes)", "Memory Management", "Exception Handling"
    ],
    "C++": [
        '#include <iostream>\nint main() {\n    std::cout << "Hello, World!" << std::endl;\n    return 0;\n}',
        'int x = 10;\nfloat y = 5.5;\nstd::string name = "Alice";',
        'int x = 10;\nif (x > 5) {\n    std::cout << "x is greater than 5" << std::endl;\n} else {\n    std::cout << "x is less than or equal to 5" << std::endl;\n}',
        'for (int i = 0; i < 5; ++i) {\n    std::cout << i << std::endl;\n}',
        'int add(int a, int b) {\n    return a + b;\n}\nint main() {\n    std::cout << add(3, 5) << std::endl;\n}',
        'class Person {\npublic:\n    std::string name;\n    int age;\n    Person(std::string n, int a) : name(n), age(a) {}\n    void introduce() {\n        std::cout << "My name is " << name << " and I am " << age << " years old." << std::endl;\n    }\n};\nint main() {\n    Person person("Alice", 30);\n    person.introduce();\n}',
        'int* ptr = new int(5);\nstd::cout << *ptr << std::endl;\ndelete ptr;',
        'try {\n    throw std::runtime_error("Something went wrong");\n} catch (const std::exception& e) {\n    std::cout << e.what() << std::endl;\n}'
    ],
    "Kotlin": [
        'fun main() {\n    println("Hello, World!")\n}',
        'val x: Int = 10\nval y: Float = 5.5f\nval name: String = "Alice"',
        'val x = 10\nif (x > 5) {\n    println("x is greater than 5")\n} else {\n    println("x is less than or equal to 5")\n}',
        'for (i in 0 until 5) {\n    println(i)\n}',
        'fun add(a: Int, b: Int): Int {\n    return a + b\n}\nfun main() {\n    println(add(3, 5))\n}',
        'class Person(val name: String, val age: Int) {\n    fun introduce() {\n        println("My name is $name and I am $age years old.")\n    }\n}\nfun main() {\n    val person = Person("Alice", 30)\n    person.introduce()\n}',
        'val number = 5\nprintln(number)',
        'try {\n    throw Exception("Something went wrong")\n} catch (e: Exception) {\n    println(e.message)\n}'
    ]
}

# 创建 DataFrame
df_usage_manual = pd.DataFrame(data_usage_manual)


# 导出为 Excel 文件
#file_path_usage_manual = "/mnt/data/C++_vs_Kotlin_Code_Comparison_Manual.xlsx"
file_path_usage_manual = "C++_vs_Kotlin_Code_Comparison_Manual.xlsx"
df_usage_manual.to_excel(file_path_usage_manual, index=False)

file_path_usage_manual
