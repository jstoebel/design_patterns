I'm trying to work with nested blocks. Something like

```
outer_box = Box.new do
  item Box.new do
    item Product.new 'hammer', 10.0
  end
end
```

would create a box, containing a box, containing a hammer. That code however does not work as expected. I found [this library](https://github.com/piotrmurach/tty-tree) which seems to basically do the same thing

```
tree = TTY::Tree.new do
  node 'dir1' do
    node 'config.dat'
    node 'dir2' do
      node 'dir3' do
        leaf 'file3-1.txt'
      end
      leaf 'file2-1.txt'
    end
    node 'file1-1.txt'
    leaf 'file1-2.txt'
  end
end
```

Let's see if I can dig into that code to see how they did it.

