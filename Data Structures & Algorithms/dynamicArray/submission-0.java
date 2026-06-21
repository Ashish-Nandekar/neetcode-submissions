class DynamicArray {
    private int[] arr;
    private int capacity;
    private int size;
    //initialize empty array
    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.arr = new int[this.capacity];
    }
    //return i-th element
    public int get(int i) {
        return arr[i];
    }
    //insert element n at i-th position
    public void set(int i, int n) {
        arr[i] = n;
    }
    //insert at end and double the array if size == to capacity
    public void pushback(int n) {
        if (size == capacity) {
            resize();
        }
        arr[size] = n;
        size += 1;
    }
    //soft delete the last element
    public int popback() {
        if(size > 0){
        size -= 1;
        }
        return arr[size];
    }
    //double the size of array
    public void resize() {
        capacity *= 2;
        int[] new_arr = new int[capacity];

        for (int i = 0; i < size; i++) {
            new_arr[i] = arr[i];
        }

        arr = new_arr;
    }
    //return the current present element
    public int getSize() {
        return size;
    }
    //return the actual capacity of array
    public int getCapacity() {
        return capacity;
    }
}
