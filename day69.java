import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Collections;
class Student implements Comparable<Student> {
    private int id;
    private String name;
    private double cgpa;

    public Student(int id, String name, double cgpa) {
        this.id = id;
        this.name = name;
        this.cgpa = cgpa;
    }

    public int getID() {
        return id;
    }

    public String getName() {
        return name;
    }

    public double getCGPA() {
        return cgpa;
    }

    @Override
    public int compareTo(Student other) {
        if (this.cgpa != other.cgpa) {
            return Double.compare(other.cgpa, this.cgpa); // Higher CGPA comes first
        } else if (!this.name.equals(other.name)) {
            return this.name.compareTo(other.name); // If CGPA is equal, compare by name
        } else {
            return Integer.compare(this.id, other.id); // If CGPA and name both are equal, compare by ID
        }
    }
}

class Priorities {
    public List<Student> getStudents(List<String> events) {
        List<Student> students = new ArrayList<>();
        
        for (String event : events) {
            String[] parts = event.split(" ");
            if (parts[0].equals("ENTER")) {
                String name = parts[1];
                double cgpa = Double.parseDouble(parts[2]);
                int id = Integer.parseInt(parts[3]);
                students.add(new Student(id, name, cgpa));
            } else if (parts[0].equals("SERVED")) {
                if (!students.isEmpty()) {
                    Collections.sort(students); // Sorting the students based on priority
                    students.remove(0); // Remove the highest priority student
                }
            }
        }

        return students;
    }
}

public class Solution {
    private final static Scanner scan = new Scanner(System.in);
    private final static Priorities priorities = new Priorities();
    
    public static void main(String[] args) {
        int totalEvents = Integer.parseInt(scan.nextLine());    
        List<String> events = new ArrayList<>();
        
        while (totalEvents-- != 0) {
            String event = scan.nextLine();
            events.add(event);
        }
        
        List<Student> students = priorities.getStudents(events);
        
        if (students.isEmpty()) {
            System.out.println("EMPTY");
        } else {
            for (Student st: students) {
                System.out.println(st.getName());
            }
        }
    }
}
