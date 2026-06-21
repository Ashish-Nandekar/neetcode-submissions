class DynamicArray {
    private int[] arr;
    private int capacity;
    private int size;
    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.arr = new int[this.capacity];
    }

    public int get(int i) {
        return arr[i];
    }

    public void set(int i, int n) {
        arr[i] = n;
    }

    public void pushback(int n) {
        if (size == capacity) {
            resize();
        }
        arr[size] = n;
        size += 1;
    }

    public int popback() {
        if(size > 0){
        size -= 1;
        }
        return arr[size];
    }

    public void resize() {
        capacity = 2 * capacity;
        int[] new_arr = new int[capacity];

        for (int i = 0; i < size; i++) {
            new_arr[i] = arr[i];
        }

        arr = new_arr;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return capacity;
    }
}
