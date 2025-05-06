
from LinkedListForChaining import LLNode,LinkedList

class HashMapUsingChaining:
    def __init__(self,capacity=13):
        self.capacity = capacity
        self.size=0
        self.buckets = self.__create_buckets(self.capacity)

    def __create_buckets(self,capacity):
        buckets = [LinkedList() for i in range(capacity)]
        return buckets
    
    def hash_function(self,key):
        return abs(hash(key)) % self.capacity

    def rehash(self):
        # print("Rehashing ...")
        old_buckets = self.buckets
        self.capacity = self.capacity*2
        self.buckets = self.__create_buckets(self.capacity)
        self.size = 0 # Reset Size before reinserting elements

        for eachLinkedListHead in old_buckets:
            current = eachLinkedListHead.head
            while current is not None:
                self.insert(current.key,current.value)
                current = current.next



    def insert(self,key,value):
        bucket_index = self.hash_function(key)
        bucket = self.buckets[bucket_index]

        node = bucket.search(key)

        if node is None:
            bucket.add(key,value)
            self.size +=1
        else:
            node.value = value # update existing Key with New Value

        load_factor = self.size / self.capacity

        # print("Load Factor", load_factor)
        if(load_factor > 0.75):
            self.rehash()
            # print("Rehashing Done")

    def get(self,key):
        bucket_index = self.hash_function(key)
        bucket = self.buckets[bucket_index]

        node = bucket.search(key)
        if(node is not None):
            return node.value
        else:
            return "Key not found"
        
    def remove(self,key):
        bucket_index = self.hash_function(key)
        bucket = self.buckets[bucket_index]

        removed = bucket.delete(key)
        if(removed ==True):
            self.size-=1
            print(f"Key {key} is removed from Hashmap")
        else:
            print(f"Key {key} not found in Hashmap")
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        for i in range(self.capacity):
            if(self.buckets[i] != None):
                self.buckets[i].traverse()
            
        return ""
    
    def __setitem__(self,key,value):
        return self.insert(key,value)



hash_map = HashMapUsingChaining(3)
# print((hash_map))
hash_map.insert("Apple",100)
hash_map.insert("Orange",105)
hash_map.insert("banana",200)
hash_map.insert("banana2",200) # 0.8
hash_map.insert("banana3",200)

# print((hash_map))
print(hash_map.get("Apple")) # Key should be case sensitive
print(hash_map.get("Orange"))
print(hash_map.get("banana"))

hash_map.remove("Apple")
print(hash_map.get("Apple")) 
print(len(hash_map))
print(hash_map)

