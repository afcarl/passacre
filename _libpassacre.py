import cffi


ffi = cffi.FFI()
ffi.cdef("""

enum passacre_gen_algorithm {
    PASSACRE_KECCAK,
    PASSACRE_SKEIN,
    ...
};

struct passacre_gen_state;

size_t passacre_gen_size(void);
size_t passacre_gen_align(void);
size_t passacre_gen_scrypt_buffer_size(void);
int passacre_gen_init(
    struct passacre_gen_state *, enum passacre_gen_algorithm);
int passacre_gen_use_scrypt(
    struct passacre_gen_state *,
    uint64_t, uint32_t, uint32_t, unsigned char *);
int passacre_gen_absorb_username_password_site(
    struct passacre_gen_state *, const unsigned char *, size_t,
    const unsigned char *, size_t, const unsigned char *, size_t);
int passacre_gen_absorb_null_rounds(struct passacre_gen_state *, size_t);
int passacre_gen_squeeze(struct passacre_gen_state *, unsigned char *, size_t);
void passacre_gen_finished(struct passacre_gen_state *);

""")

preamble = '#include "passacre.h"'
