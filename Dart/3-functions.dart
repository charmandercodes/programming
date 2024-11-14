void main() {
  final greeting = greet(age: 25, name: "mario");
  print(greeting);
}

String greet({required String name, required int age}) {
  return "Hi,my age is $age my name is $name and I am $age";
}


