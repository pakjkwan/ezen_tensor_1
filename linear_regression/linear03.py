import tensorflow as tf
tf.set_random_seed(777)

W = tf.Variable(tf.random_normal([1]),name = 'weight') # 가중치
b = tf.Variable(tf.random_normal([1]),name='bias')


# placeholder 에 의한 방식

X = tf.placeholder(tf.float32, shape=[None])
Y = tf.placeholder(tf.float32, shape=[None])

hypothesis = X * W + b
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# 비용함수의 최소화 minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)
# train 은 노드가 되고 이것을 실행해야 한다.
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# fit the line 최적화
for step in range(2001):
    cost_val , W_val, b_val, _  = \
    sess.run([cost, W, b, train],
             feed_dict={X:[1,2,3], Y:[1,2,3]} )
    if step % 20 == 0:
        print(step, cost_val, W_val, b_val)













