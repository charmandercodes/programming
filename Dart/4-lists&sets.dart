void main() {
  // LISTS

  List<int> scores = [50, 75, 20, 99];

  print("// Changing");
  scores[0] = 25;
  print('${scores[0]}\n');

  print("// Adding");
  scores.add(100);
  print('$scores\n');

  print("// Removing");
  scores.remove(20);
  print('$scores\n');

  print("// Removing Last");
  scores.removeLast();
  print('$scores\n');

  print("// Shuffling");
  scores.shuffle();
  print('$scores\n');

  print("// Index of 99");
  print('${scores.indexOf(99)}\n');

  // SETS - cannot have duplicates

  Set<String> names = {"mario", "luigi", "peach"};

  names.add("bowser");
  names.add("peach");
  names.remove("luigi");
  print(names);
  print(names.length);
}
