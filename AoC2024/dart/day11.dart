// --- Day 11: Plutonian Pebbles ---
import 'dart:io';

final test1 = [125, 17];

int part1(List<num> line, int blink) {
  var current = [...line];
  for (var i = 0; i < blink; i++) {
    print("Iteration $i");
    var new_line = <num>[];
    for (final value in current) {
      if (value == 0) {
        new_line.add(1);
      } else if (value.toString().length % 2 == 0) {
        final String vstr = value.toString();
        new_line.add(num.parse(vstr.substring(0, vstr.length ~/ 2)));
        new_line.add(num.parse(vstr.substring(vstr.length ~/ 2, vstr.length)));
      } else {
        new_line.add(value*2024);
      }
    }
    print("new: ${new_line.length}");
    current = [...new_line];
  }
  return current.length;
}



int part2(List<num> line, int blink) {
  print(line.map((e) => e.toString()).join('\n'));
  final c = File('current.txt').writeAsStringSync(line.map((e) => e.toString()).join('\n'));
  for (var i = 0; i < blink; i++) {
    print("*** blink $i ***");
    // final File('new.txt').createSync();
    final new_line = File('new.txt');
    final current = File('current.txt');
    for (final vstr in current.readAsLinesSync()) {
      int value = int.parse(vstr);
      String str = value.toString();
      // print(value);
      if (value == 0) {
        // print('$value -> 1');
        new_line.writeAsStringSync('1\n', mode: FileMode.append);
      } else if (str.length % 2 == 0) {
        // print('$value -> /2 /2');
        new_line.writeAsStringSync('${str.substring(0, str.length ~/ 2)}\n', mode: FileMode.append);
        new_line.writeAsStringSync('${str.substring(vstr.length ~/ 2, str.length)}\n', mode: FileMode.append);
      } else {
        // print('$value -> *2024');
        new_line.writeAsStringSync('${value*2024}\n', mode: FileMode.append);
      }
    }
    current.deleteSync();
    new_line.copySync('current.txt');
    new_line.deleteSync();
  }
  final current = File('current.txt');
  return current.readAsLinesSync().length;
}

void main() {
  // print ("test 1 by 6 iteration: ${part1(test1, 6)}");
  // print ("test 1 by 25 iteration: ${part1(test1, 25)}");

  String input = File('../datas/day11.txt').readAsStringSync();
  var list = List<num>.from(input.split(' ').map((e) => num.parse(e)));
  // print ("Part 1 input by 25 iteration: ${part1(list, 25)}");
  print ("Part 2 input by 75 iteration: ${part2(list, 75)}");
}
