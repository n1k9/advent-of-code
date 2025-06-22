import 'dart:io';


void main() {
  var input = File('datas/data-01-1.txt').readAsLinesSync();
  assert(part1([3,4,2,1,3,3], [4,3,5,3,9,3]) == 11);
  var list1 = List<int>.from(input.map((e) => int.parse(e.replaceAll('   ', ' ').split(' ')[0])));
  var list2 = List<int>.from(input.map((e) => int.parse(e.replaceAll('   ', ' ').split(' ')[1])));
  print('Part 1: ${part1(list1, list2)}');
  print('Part 2: ${part2(list1, list2)}');
}

int part1(List<int> list1, List<int> list2) {
  list1.sort();
  list2.sort();
  var sum = 0;
  for (var i = 0; i < list1.length; i++) {
    sum += (list1[i] - list2[i]).abs();
  }
  return sum;
}

int part2(List<int> list1, List<int> list2) {
  return list1.map((e) => e * list2.where((i) => i == e).length).reduce((value, element) => value + element).toInt();
}

