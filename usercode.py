import jwt


payload_data = {
  "iat": 1670696872,
  "exp": 1670696872,
  "application_id": "3b7ce5ac-48b8-41f0-8e1f-5b0ca1e1cf61"
}

key = "-----BEGIN PRIVATE KEY-----iMIIEuwIBADANBgkqhkiG9w0BAQEFAASCBKUwggShAgEAAoIBAQCfA78LDmBPgM1TijYg0Xmadnj2rRhx94Pxu9C3NqevpF2MIQ99Plv/NGYV2Sjgf9jRhuCEkUL+RoFcYiNRc8fwW5Fa/FXgbjzza8XfYhJlbzwIax0kDF6IT36NGjc1ZYfQ/2TgwO1WOvYWr8ij5pveSmcHiWjhoG8TyoYM2hK2zHCNz02oTW7VACaKghn9Cq57x0b66h8De+Vp1nmimvY+37oTcej7ZWrz7co96loNd1ePjeEtpdBSJApSOrCsyiL73XAvz4wKEqXlVfnhiBmhIhp6Z+dRfjRKROyYhFpdlDNck+Qe36npW+TINF6JydQfqOR88wvZt1qLhtz5giK3ywVlbnAgMBAAECgf91tNA13u5r62wR7TJlkXtkMT51CfENPP2fJCDDnISEhktIiUvV6dMvlhn7EkSv6fMVJkIL33s3vfkD6KlKI9X3HA8aY0oFHIJvj06nd4AN9a4ZJiGtnXpcbHvA9ybm38Epc+O4exc0PXDsWjLqmi2o1ygt5ZrbdbLT57q5IH1zl+CTlkiHEgxynbswOJdBwUxxDOX+Uospxtb1RxsxDSp7cwYHIeAqIg4t5hqE7OUm1btAx/ViSxUecrInxHKSfrMtFXH2ty0KrtLunopknsDie3ixyf9XEkNd9H4TQq0zn2e8aKKbiatFy9iR+p2FU+12fU1QJzzpuE3x75FtZyLun4dUCgYEA4FlyK1FN66HF1YvrBj2+i3TZfGof/8hwvcpS81eX0a0KExNHg2L0a/c+vPRC+8xric99zjIwcbb2pTTme7dHoiAgiUj18WlNc8VCbAbHysEJpAYhb+4J+/e+3ZQaxPZbP95nX+PX6jaEuLjIdSsQm0ib0KSO0ZYR50Sf7VTbQ5ZWF0CgYEAtXKvJQVID/NeYKIQutA7336kWmsDemtdmfgyiYfYeshPrn54eh5Gsi2iYK6J3p/U1J0Qs+Zdhsrsea8WnH/5Yjy/LWNvO/fydZjexiLx/3yzojPBJs9TwqH7CIpXoxemnNX2DsVrF0vE5RfUiIvhTyLcwSppEhQYT6EWvVi6+obaBMCgYAQELepPHA9AF+fVB6nWsKRKrSSvMxqNPR82wPOuWHQUHobcgAM5TXKimRWuZMWXuQQgUg7/MIVUonE+M3MbCp33j0+8GI4QaH1MdV3wJtlXcwRLQeRMh4P5ixuV423LwEHyNBUQIeUoQTOCYVpRoUw6VrQm1rurhbfEGLiDkPVPOjQKBgQCC0WZ5iGG+2IE6A+Rd6uLsSDWpNTi45ysK3SXx5qErFNRuB/ywfreVqtURQ4VfHnkBuSPbsiFDp58/Kg3OX7aRNMWLcRH5kDAWgx1CFIypGK0iWpH9eyj2gHZO1/8LNPgIxzIZwDifPme8hBKdUsxUESyxBkGQkhpxofMm6Sl7ClKRQKBgHgyi/3uXCqHWzbj2zT7vaONiF9i08A8Rf4adx3xoe/e/v/PbGJv2BTgGMgnyMw9T9q2DjyJC7QojM0DF1v9wl4X6ihDaYNV0+4DHUd3cDPxm4x1O1FUDB57KNhaxHYksr+1f7vWbvfR+FW+vOKP9t5FRIicBZoHBWvXnt9emEAHTJDi-----END PRIVATE KEY-----"


def handle(data):

  
    data["token"]  = jwt.encode(
    payload=payload_data,
    key=key,
    algorithm='HS256'
)
    
    
    return data
